import Vue from 'vue'
import Vuex from 'vuex'

// all modules import
import CountryDataModule from './modules/countries'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    countriesData: CountryDataModule
  },
  state: {
    //
  },
  mutations: {
    //
  },
  actions: {
    //
  }
})

export default store
