<template>
  <q-page class="flex flex-center">
    <scrapeForm></scrapeForm>
    <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
  </q-page>
</template>

<style>
</style>

<script>
import scrapeForm from '../components/scrape-form'
export default {
  name: 'PageIndex',
  components: {scrapeForm}
}
</script>
