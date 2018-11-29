import Vue from 'vue'
import Vuex from 'vuex'

import scrape from './scrape'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      scrape
    }
  })

  // if we want some HMR magic for it, we handle
  // the hot update like below. Notice we guard this
  // code with "process.env.DEV" -- so this doesn't
  // get into our production build (and it shouldn't).
  if (process.env.DEV && module.hot) {
    module.hot.accept(['./scrape'], () => {
      const newScrape = require('./scrape').default
      Store.hotUpdate({ modules: { scrape: newScrape } })
    })
  }

  return Store
}
