<template>
  <div id="core-drawer-toolbar">
    <!-- toolbarr start -->
    <v-toolbar flat class="topbar" :height="height" fixed>

      <!-- <div v-if="responsive" class="topbaricon" @click.stop="drawer = !drawer">
        <v-icon>mdi-menu</v-icon>
      </div> -->

      <div class="logo">
        <!-- <img src="assets/img/logo/quarantine_notes_icon.png" alt="logo"> -->
        QUARANTINE NOTES
      </div>


      <!-- <v-spacer />

      <v-toolbar-items>
        <v-flex align-center justify-center layout>

          <v-menu  bottom left  offset-y transition="slide-y-transition" content-class="notification-menu">
            <div  slot="activator" class="toolbar-items" to="/notifications">
              <v-badge color="error" overlap>
                <template slot="badge">
                  {{ notifications.length }}
                </template>
                <v-icon style="font-size:26px;color:#fff;">mdi-bell</v-icon>
              </v-badge>
            </div>

            <v-card>
              <v-list dense>
                <v-list-tile v-for="notification in notifications" :key="notification" @click="onClick">
                  <v-list-tile-title v-text="notification"/>
                </v-list-tile>
              </v-list>
            </v-card>

          </v-menu>

          <v-menu  bottom left  offset-y transition="slide-y-transition" content-class="profile-menu">
            <v-toolbar-title slot="activator">
              <div class="avater">
                <img  src="../../assets/img/parson.png" alt="John">
              </div>
              John Doe, <span> User <i data-feather="chevron-down"></i></span>
            </v-toolbar-title>

             <v-card>
              <v-list dense>
                  <v-list-tile v-for="(item,i) in profiles" :key="i" @click="onProfileSettingClick">
                     <v-list-tile-action>
                        <i :data-feather="item.icon"></i>
                      </v-list-tile-action>
                      <v-list-tile-title v-text="item.text"/>
                  </v-list-tile>
              </v-list>
            </v-card>

          </v-menu>

        </v-flex>
      </v-toolbar-items> -->

    </v-toolbar>
    <!-- toolbar end -->

    <!-- drawer start -->
    <!-- <v-navigation-drawer v-model="drawer" app class="sidebar" :width="width">

      <div class="compose-btn">
        <v-btn :ripple="false">compose</v-btn>
      </div>

      <v-list dense> -->

        <!-- single item -->
        <!-- <v-list-tile v-for="(link, i) in links" :key="i" :to="link.to">
          <v-list-tile-action>
            <i :class="link.icon"></i>
          </v-list-tile-action>
          <v-list-tile-title v-text="link.text"/>
        </v-list-tile>

      </v-list>
    </v-navigation-drawer> -->
    <!-- drawer end -->

  </div>
</template>

<script>
  export default {
    data: () => ({
      notifications: [
        "Mike, John responded to your email",
        "You have 5 new tasks",
        "You're now a friend with Andrew",
        "Another Notification",
        "Another One"
      ],
      links: [
        {
          to: "/",
          icon: "flaticon-close-envelope",
          text: "Inbox"
        },
        {
          to: "/starred",
          icon: "flaticon-favourites-filled-star-symbol",
          text: "Starred"
        },
        {
          to: "/sentmail",
          icon: "flaticon-sent",
          text: "Sent mail"
        },
        {
          to: "/draft",
          icon: "flaticon-lines",
          text: "Draft"
        },
        {
          to: "/chat",
          icon: "flaticon-speech-message",
          text: "Chat"
        },
        {
          to: "/places",
          icon: "flaticon-house-black-silhouette-without-door",
          text: "Places"
        },
        {
          to: "/trash",
          icon: "flaticon-garbage",
          text: "Trash"
        },
        {
          to: "/spam",
          icon: "flaticon-spam",
          text: "Spam"
        }
      ],
      profiles: [
        {
          icon : 'user',
          text : 'My Profile'
        },
        {
          icon : 'message-circle',
          text : 'Message'
        },
        {
          icon : 'settings',
          text : 'Settings'
        },
        {
          icon : 'log-out',
          text : 'Logout'
        }
      ],
      drawer: null,
      width : 320,
      height: 85,
      responsive: false
    }),
    mounted () {
      this.onResponsiveMenu();
      window.addEventListener("resize", this.onResponsiveMenu);
      this.getFeatherIcon();
    },
    methods : {
      onResponsiveMenu() {
        if (window.innerWidth < 1199) {
          this.responsive = true;
        } else {
          this.responsive = false;
        }
      },
      onClick() {
        //
      },
      onProfileSettingClick () {
        //
      },
      getFeatherIcon() {
        feather.replace()
      }
    }
  }
</script>
