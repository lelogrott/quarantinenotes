<template>
  <div  class="compose-note">
    <v-container grid-list-md>

      <v-layout row wrap>
        <v-flex lg4 md6 sm12 xs12>
          <v-text-field
            v-model="name"
            :counter="20"
            :rules="nameRules"
            label="Name"
            required
          ></v-text-field>
        </v-flex>
        <v-flex lg4 md6 sm12 xs12>
          <v-select
            v-model="select"
            item-text="friendly_name"
            item-value="id"
            :items="countries"
            :rules="[v => !!v || 'Country is required']"
            label="Country"
            required
          ></v-select>
        </v-flex>
      </v-layout>
    </v-container>

    <div class="comment">
      <textarea  id="mail-comment"  placeholder="Write something..."></textarea>
      <div class="scroll-top">
        <i class="flaticon-sent-mail"></i>
      </div>
    </div>
    <br>
  </div>
</template>

<script>
export default {
  data () {
    return {
      name: null,
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 20) || 'Name must be less than 20 characters',
      ],
      select: null,
      countries: this.$store.state.countriesData.countriesInfo
    }
  }
}
</script>
