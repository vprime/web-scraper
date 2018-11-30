import axios from 'axios'

export const scrape = ({ commit, state }) => {
  console.log(process.env.API)
  axios
    .post(process.env.API + '/scrape', {
      address: state.url
    })
    .catch(error => {
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        console.log(error.response.data)
        console.log(error.response.status)
        console.log(error.response.headers)
      } else if (error.request) {
        // The request was made but no response was received
        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
        // http.ClientRequest in node.js
        console.log(error.request)
      } else {
        // Something happened in setting up the request that triggered an Error
        console.log('Error', error.message)
      }
      console.log(error.config)
    })
    .then(request => request.data)
    .then(scrape => {
      commit('addScan', scrape)
    })
}

export const clearUrl = ({ commit }) => {
  commit('clearUrl')
}
