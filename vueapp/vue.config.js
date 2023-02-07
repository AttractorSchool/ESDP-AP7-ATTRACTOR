const path = require('path');

module.exports = {
    publicPath: '/static/src/vue/dist/', // Should be STATIC_URL + path/to/build
    outputDir: path.resolve(__dirname, '../static/src/vue/dist/'), // Output to a directory in STATICFILES_DIRS
    filenameHashing: false, // Django will hash file names, not webpack
    runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
    devServer: {
        devMiddleware: {
            // see https://github.com/webpack/webpack-dev-server/issues/2958
            writeToDisk: true,
        }
    },
};