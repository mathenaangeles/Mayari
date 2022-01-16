module.exports = {
  configureWebpack: {
    devServer: {
      port: 8080,
      // https://github.com/vuejs-templates/webpack/issues/378
      watchOptions: {
        poll: 1000,
        aggregateTimeout: 300
      },
    },
  },
  pwa: {
    iconPaths: {
      favicon32: "favicon.ico",
      favicon16: "favicon.ico",
      appleTouchIcon: "favicon.ico",
      maskIcon: "favicon.ico",
      msTileImage: "favicon.ico",
    },
  },
};
