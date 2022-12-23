module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: `${process.env.PORT}/api/`,
        changeOrigin: true,
        pathRewrite: {
          "^/api": "",
        },
      },
    },
  },
  outputDir: "../backend/dist",
};
