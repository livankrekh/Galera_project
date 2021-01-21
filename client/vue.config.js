const webpack = require('webpack');

module.exports = {
  configureWebpack: {
    // Set up all the aliases we use in our app.
    plugins: [
      new webpack.optimize.LimitChunkCountPlugin({
        maxChunks: 6
      })
    ]
  },
  pwa: {
    name: 'Kyocera',
    themeColor: '#e0011c',
    msTileColor: '#e0011c',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: '#e0011c'
  },
  css: {
    // Enable CSS source maps.
    sourceMap: process.env.NODE_ENV !== 'production'
  }
};
