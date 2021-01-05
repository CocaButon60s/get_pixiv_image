<template>
  <div class="row m-5">
      <div class="col text-center">
          <b-button variant="primary" :disabled=isLoading @click="click">
              <div class="text" v-show="!isLoading"><slot/></div>
              <div class="spinner" v-show="isLoading">
                  <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                  <span>Loading...</span>
              </div>
          </b-button>
      </div>
  </div>
</template>

<script>
export default {
  name: 'InputForm',
  props: {
    isLoading: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    click () { this.$emit('callback') }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
