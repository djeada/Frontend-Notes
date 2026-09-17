import {defineConfig} from '@playwright/test';
export default defineConfig({
  testDir: './tests',
  testMatch: '**/*.spec.mjs',
  fullyParallel: true,
  retries: 0,
  reporter: [['list']],
  use: {baseURL:'http://127.0.0.1:4173', browserName:'chromium', trace:'retain-on-failure', screenshot:'only-on-failure'},
  webServer: {command:'node server.mjs', url:'http://127.0.0.1:4173', reuseExistingServer: !process.env.CI, timeout:30000},
});
