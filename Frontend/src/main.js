import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'
import VueResource from 'vue-resource'
import vuetify from './plugins/vuetify'
import HelloWorld from './components/HelloWorld';
import User from './components/user'
import Register from './components/signup'
import GetValue from './components/get'
import SetValue from './components/set'
import GAuth from 'vue-google-oauth2'



Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(Router)

const gauthOption = {
  clientId: '478091043171-lhojfm5rhienbr1j7jqrd99611nihovv.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'select_account'
}
Vue.use(GAuth, gauthOption)


const router = new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: HelloWorld
    },
    {
      path: '/index/',
      name: 'home',
      component: User
    },
    {
    	path: '/getvalue/',
    	name: 'get',
    	component: GetValue
    },
    {
      path: '/setvalue/',
      name: 'set',
      component: SetValue
    },
    {
      path: '/signup',
      name: 'register',
      component: Register
    }
  ]
})

new Vue({
  vuetify,
  router: router,
  render: h => h(App)
}).$mount('#app')


