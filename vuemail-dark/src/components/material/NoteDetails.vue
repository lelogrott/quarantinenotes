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
  </div>
</template>

<script>
  export default {
    props: {
      noteDetailsData: {
        type : Object,
        default: () => {}
      }
    },
    mounted(){
      this.scrollToTop();
    },
    methods: {
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
