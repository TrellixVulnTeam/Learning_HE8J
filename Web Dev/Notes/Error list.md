React -

error export path not ...

If you use yarn you can:

```shell
rm -rf node_modules yarn.lock
yarn add -D react-scripts@latest
yarn build
```

For npm:

```bash
rm -rf node_modules package-lock.json
npm install -D react-scripts@latest
npm install
npm run build
```