<template>
  <div>
    <div>My component</div>
    <section class="main">
      <input v-model="url" placeholder="Scrape Url" v-on:keyup.enter="scanUrl($event)" />

      <ul class="scrapes-list">
        <li v-for="scrape in scans"
          class="scrape"
          :key="scrape.id">
          <div class="view">
            <span>Scan: {{scrape.source}}</span>
            <label>{{scrape.status}}</label>
            <p></p>
          </div>
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
import { mapState, mapMutations, mapGetters } from 'vuex'

export default {
  name: 'ScrapeForm',
  data () {
    return {
      url: ''
    }
  },
  created () {

  },
  computed: {
    ...mapState('scrape', ['scrapes']),
    ...mapGetters('scrape', ['scans'])
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
