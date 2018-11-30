<template>
  <form>
    <label>Scrape a Page</label>
    : <input v-model="url" placeholder="Scrape Url" v-on:keyup.enter="scanUrl($event)" />
  </form>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  name: 'ScrapeForm',
  data () {
    return {
      url: ''
    }
  },
  created () {
  },
  methods: {
    ...mapMutations('scrape', ['setUrl']),
    scanUrl (e) {
      const text = e.target.value
      this.setUrl(text)
      this.$store.dispatch('scrape/scrape')
    }
  }
}
</script>

<style>
</style>
