<template>
  <ul class="scrapes-list">
    <li v-for="scrape in scans"
      class="scrape"
      :key="scrape.id">
      <div class="view">
        <span>Scan: {{scrape.source}}</span>
        <label>{{scrape.status}}</label>
        <p>
          <ul>
            <li v-for="address in scrape.detections" :key="address.id">
              <ScrapedURL :address=address :source=scrape.source></ScrapedURL>
            </li>
          </ul>
        </p>
      </div>
    </li>
  </ul>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
import ScrapedURL from './scraped-url'
export default {
  // name: 'ComponentName',
  data () {
    return {}
  },
  computed: {
    ...mapState('scrape', ['scrapes']),
    ...mapGetters('scrape', ['scans'])
  },
  components: {
    ScrapedURL
  }
}
</script>

<style>
</style>
