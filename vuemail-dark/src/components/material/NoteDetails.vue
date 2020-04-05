<template>
  <div  class="single-note-details-item">
    <div class="head-part">
      <div class="head-top">
        <h2>{{noteDetailsData.author}}</h2>
        <div class="time">
          {{new Date(noteDetailsData.createdAt) | moment("dddd, MMMM Do YYYY, h:mm:ss A") }}
        </div>
      </div>
      <div class="head-subject">
        {{getCountry(noteDetailsData.country)}}
      </div>
    </div>
    <div class="body-part">
      <p>
        {{noteDetailsData.content}}
      </p>
    </div>


    <div class="card-left-side-ui-design">
      <div class="card-index active" v-for="(item,i) in this.noteDetailsData.replies" :key="i">
        <div class="card-info">
          <div class="card-head">
            <h3><a>{{item.author}}</a></h3>
            <div class="card-date">{{new Date(item.createdAt) | moment("MMM Do h:mmA") }}</div>
          </div>
          <a>{{getCountry(item.country)}}</a>
          <div class="card-para">
            {{item.content}}
          </div>
        </div>
      </div>
    </div>

    <compose-note
      :key='composeReplyKey'
      :options="this.replyOptions()"
    />

  </div>
</template>

<script>
  import EventBus from './../../eventBus.js'

  export default {
    data() {
      return {
        composeReplyKey: 0
      }
    },
    props: {
      noteDetailsData: {
        type : Object,
        default: () => {}
      }
    },
    mounted(){
      var vm = this;
      this.scrollToTop();

      EventBus.$on('reply-added', function (reply) {
        vm.insertReply(reply.data);
        vm.composeReplyKey += 1;
      });
    },
    methods: {
      replyOptions() {
        return {
          noteId: this.noteDetailsData.noteId,
          placeholder: 'What do you think about it?'
        };
      },
      insertReply(reply) {
        this.noteDetailsData.replies.push(reply);
      },
      scrollToTop() {
        $('.scroll-top').on('click',function(){
            $('html, body').animate({
            scrollTop: 0
          }, 1500);
          return false;
        });
      },
      getCountry(id) {
        let countries = this.$store.state.countriesData.countriesInfo;
        for (var i = countries.length - 1; i >= 0; i--) {
          if (id == countries[i].id)
            return countries[i].friendly_name;
        }
        return 'Unknown';
      }
    }
  }
</script>
