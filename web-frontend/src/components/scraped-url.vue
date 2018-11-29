<template>
  <div>
    <a :href="address">{{address}}</a>
    Source:<a :href="source">go</a>
  </div>
</template>

<script>
export default {
  // name: 'ComponentName',
  props: ['address', 'source']
}
</script>

<style>
</style>
