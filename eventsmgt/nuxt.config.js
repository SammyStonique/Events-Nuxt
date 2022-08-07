export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'eventsmgt',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel:'stylesheet',
        href:'https://fonts.googleapis.com/css?family=Montserrat:400,800',
        // href:"https://fonts.googleapis.com/css?family=Open+Sans:300,400|Source+Code+Pro:700,900&display=swap",  
      },
      {
        rel:'stylesheet',
        href:"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
      }
      
    ],
    script: [
      {
        crossorigin: 'anonymous',
        src: "https://kit.fontawesome.com/45760a6434.js",
      },
      {
        crossorigin: 'anonymous',
        src: "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js",
      }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    '@nuxtjs/vuetify',
    // '@nuxtjs/router-extras',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    '@nuxtjs/toast',
    
  ],

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  },
  //Axios configuration
  // add this Axios object
  axios: {
    baseURL: "http://localhost:8000/api/v1/",
  },
  auth: {
    strategies: {
        local: {
          scheme: 'refresh',
          token: {
            property: 'access_token',
            maxAge: 1800,
            global: true,
            // type: 'Bearer'
          },
          refreshToken: {
            property: 'refresh_token',
            data: 'refresh_token',
            maxAge: 60 * 60 * 24 * 30
          },
          endpoints: {
              login: {
                  url: 'token/',
                  method: 'post',
                  propertyName: 'access',
                  altProperty: 'refresh'
              },
              refresh: { url: 'token/refresh/', method: 'post', propertyName: 'refresh', },
              logout: {},
              user: false
            }
        }
    },
    redirect: {
        login: 'login',
    },
},
// router: {
//     middleware: ['auth']
// },

  toast: {
    position: 'top-center',
    iconPack: 'fontawesome',
    duration: 3000,
    register: [
      {
        name: 'defaultSuccess',
        message: (payload) =>
          !payload.msg ? 'Operation Succesful' : payload.msg,
        options: {
          type: 'success',
          icon: 'check'
        }
      },
      {
        name: 'defaultError',
        message: (payload) =>
          !payload.msg ? 'Oops.. Operation Failed' : payload.msg,
        options: {
          type: 'error',
          icon: 'times'
        }
      }
    ]
  },

}
