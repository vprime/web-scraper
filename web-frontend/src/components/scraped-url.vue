<template>
  <div>
    <a :href="address">{{address}}</a> <button v-on:click="scanUrl(address)">scan</button>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  // name: 'ComponentName',
  props: ['address'],
  methods: {
    ...mapMutations('scrape', ['setUrl']),
    scanUrl (url) {
      this.setUrl(url)
      this.$store.dispatch('scrape/scrape')
    }
  }
}
</script>

<style>
</style>
