<template>
  <div class="sent-mail">
    <v-container grid-list-md>
      <v-layout row wrap>

        <v-flex lg4 md12 sm12 xs12>
          <div class="card-left-side card-left-side-ui-design">

            <div class="card-index" v-for="(item,i) in sentData" :key="i">
              <div class="card-circle" :class="item.category"></div>
              <div class="card-info">
                <div class="crad-head">
                  <h3><router-link to="">{{item.title}}</router-link></h3>
                  <div class="card-date">{{item.time}}</div>
                </div>
                <div class="card-para">
                  {{item.para}}
                </div>
              </div>
            </div>

          </div>
        </v-flex>

        <v-flex lg8 md12 sm12 xs12>
          <div class="card-right-side card-left-side-ui-design">
            <single-mail-details :emailDetailsData="sentData" />
          </div>
        </v-flex>

      </v-layout>
    </v-container>
  </div>
</template>

<script>

  export default {
    name: 'sent-mail',
    computed : {
      emailsData() {
        return this.$store.state.emailsData.emailsInfo
      },
      sentData() {
        let newVariable = this.$store.state.emailsData.emailsInfo;

        return newVariable.filter(item => {
          return item.category === 'sent'
        })
      }
    }
  }
</script>
