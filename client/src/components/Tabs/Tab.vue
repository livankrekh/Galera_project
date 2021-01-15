<template>
  <div class="tab-pane"
       v-show="active"
       :id="id || title"
       :class="{active: active}">
    <slot></slot>
  </div>
</template>
<script>

</script>
<style>
</style>
