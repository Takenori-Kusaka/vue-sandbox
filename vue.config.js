module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/sandbox/'
    : '/',
  transpileDependencies: [
    'vuetify'
  ]
}
