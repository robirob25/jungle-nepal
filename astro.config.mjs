import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  build: {
    format: 'file'
  },
  server: {
    port: 8088,
    host: true
  }
});
