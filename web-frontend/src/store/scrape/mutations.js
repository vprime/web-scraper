
export const addScan = (state, scan) => {
  console.log(state.scans)
  console.log(scan)
  state.scans.push(scan)
}

export const setScans = (state, scans) => {
  state.scans = scans
}

export const clearScans = (state) => {
  state.scans = []
}

export const setUrl = (state, url) => {
  if (!url.match(/^[a-zA-Z]+:\/\//)) {
    url = 'http://' + url
  }
  state.url = url
}

export const clearUrl = (state) => {
  state.url = ''
}
