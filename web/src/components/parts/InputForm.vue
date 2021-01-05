<template>
  <div class="row m-5">
    <div class="col text-center">
      <label>
        <slot/>
        <b-form-input type="text" class="form-control" :value="contents" @change="update">
      </label>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InputForm',
  props: {
    contents: {
      type: String,
      required: true
    }
  },
  methods: { update: function (e) { this.$emit('update:contents', e) } }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
