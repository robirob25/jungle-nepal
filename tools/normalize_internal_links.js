import fs from 'fs';
import path from 'path';

function walk(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    file = path.join(dir, file);
    const stat = fs.statSync(file);
    if (stat && stat.isDirectory()) {
      results = results.concat(walk(file));
    } else if (file.endsWith('.astro') || file.endsWith('.json')) {
      if (!file.includes('node_modules') && !file.includes('.astro/')) {
        results.push(file);
      }
    }
  });
  return results;
}

const files = walk('src');
let totalModified = 0;
let totalReplacedLinks = 0;

for (const file of files) {
  let content = fs.readFileSync(file, 'utf8');
  let original = content;

  // 1. Static hrefs without slash: href="/tours/xyz", href="/en/tours/xyz", href="/destinations/xyz", href="/blog/xyz"
  content = content.replace(/href="(\/(?:en\/)?(?:tours|destinations|blog|safari-nepal)(?:\/[a-zA-Z0-9_\-]+)?)"/g, (m, p1) => {
    totalReplacedLinks++;
    return `href="${p1}/"`;
  });

  // 2. Static static pages: contact, about, mentions-legales
  content = content.replace(/href="(\/(?:en\/)?(?:contact|a-propos|about|mentions-legales|legal-mentions))"/g, (m, p1) => {
    totalReplacedLinks++;
    return `href="${p1}/"`;
  });

  // 3. Exact href="/en" -> href="/en/"
  content = content.replace(/href="\/en"/g, () => {
    totalReplacedLinks++;
    return 'href="/en/"';
  });

  // 4. Dynamic template strings with prefix
  content = content.replace(/href=\{`\$\{prefix\}\/(tours|destinations|blog)(\/[a-zA-Z0-9_\-]+)?`\}/g, (m, p1, p2) => {
    totalReplacedLinks++;
    return `href={\`\${prefix}/${p1}${p2 || ''}/\`}`;
  });

  // 5. Dynamic tour.slug links
  content = content.replace(/href=\{`\/tours\/\$\{tour\.slug\}`\}/g, () => {
    totalReplacedLinks++;
    return 'href={`/tours/${tour.slug}/`}';
  });
  content = content.replace(/href=\{`\/en\/tours\/\$\{tour\.slug\}`\}/g, () => {
    totalReplacedLinks++;
    return 'href={`/en/tours/${tour.slug}/`}';
  });

  // 6. onclick window.location.href='/tours/${tour.slug}'
  content = content.replace(/window\.location\.href='\/tours\/\$\{tour\.slug\}'/g, () => {
    totalReplacedLinks++;
    return "window.location.href=`/tours/${tour.slug}/`";
  });
  content = content.replace(/window\.location\.href='\/en\/tours\/\$\{tour\.slug\}'/g, () => {
    totalReplacedLinks++;
    return "window.location.href=`/en/tours/${tour.slug}/`";
  });

  // 7. Header nav variables:
  // const destUrl = currentLang === 'en' ? '/en/destinations' : '/destinations';
  // const aboutUrl = currentLang === 'en' ? '/en/about' : '/a-propos';
  // const blogUrl = currentLang === 'en' ? '/en/blog' : '/blog';
  // const contactUrl = currentLang === 'en' ? '/en/contact' : '/contact';
  if (file.endsWith('Header.astro')) {
    content = content.replace("'/en/destinations' : '/destinations'", "'/en/destinations/' : '/destinations/'");
    content = content.replace("'/en/about' : '/a-propos'", "'/en/about/' : '/a-propos/'");
    content = content.replace("'/en/blog' : '/blog'", "'/en/blog/' : '/blog/'");
    content = content.replace("'/en/contact' : '/contact'", "'/en/contact/' : '/contact/'");
  }

  // Double slash safety check: fix any href="...//" accidental double slashes
  content = content.replace(/href="([^"?#]+)\/\/"/g, 'href="$1/"');

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    totalModified++;
  }
}

console.log(`Successfully normalized ${totalReplacedLinks} links across ${totalModified} files.`);
