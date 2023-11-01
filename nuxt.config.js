export default {

  generate: {
    fallback: true
  },

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Potisen - Election & Political Nuxt Template',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {hid: 'description', name: 'description', content: ''}
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/assets/images/favicons/favicon-32x32.png'},
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css?family=Barlow:300,400,500,600,700,800,900%7CLibre+Baskerville:400,700&display=swap"
      },
      {rel: "stylesheet", href: "/assets/css/animate.min.css"},
      {rel: "stylesheet", href: "/assets/css/bootstrap.min.css"},
      {rel: "stylesheet", href: "/assets/css/bootstrap-select.min.css"},
      {rel: "stylesheet", href: "/assets/css/font-awesome.min.css"},
      {rel: "stylesheet", href: "/assets/plugins/potisen-icons/style.css"},
      {rel: "stylesheet", href: "/assets/plugins/glightbox/glightbox.min.css"},
      {rel: "stylesheet", href: "/assets/css/style.css"},
      {rel: "stylesheet", href: "/assets/css/responsive.css"},
    ],

    script: [
      {src: "/assets/plugins/glightbox/glightbox.min.js", body: true},
      {src: "/assets/plugins/accordion/accordion.min.js", body: true},
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: {color: '#d41e44', height: '4px'},

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    {src: 'plugins/typed.js', ssr: true},
    {src: 'plugins/owl.js', ssr: false},
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [],

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {}
}
