<template>
  <q-page class="flex flex-center">
    <div>
      <ScrapeForm></ScrapeForm>
    </div>
    <div>
      <ScrapeList></ScrapeList>
    </div>
    <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
  </q-page>
</template>

<style>
</style>

<script>
import ScrapeForm from '../components/scrape-form'
import ScrapeList from '../components/scrape-list'
export default {
  name: 'PageIndex',
  components: {ScrapeForm, ScrapeList}
}
</script>
