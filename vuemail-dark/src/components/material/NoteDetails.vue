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
        <!-- {{noteDetailsData.subject}} -->
        Subject
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
      }
    }
  }
</script>

