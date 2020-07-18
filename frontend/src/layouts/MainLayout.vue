<template>
  <q-layout view="lHh Lpr fff" class="bg-white" >
    <q-header elevated class="bg-grey-10 rounded-borders shadow-2" height-hint="64" v-if="$q.platform.is.mobile">
      <div v-if="!$route.fullPath.includes('/auth')">
        <q-toolbar style="height: 64px">
          <q-btn
            flat
            dense
            round
            @click="leftDrawerOpen = !leftDrawerOpen"
            aria-label="Menu"
            color="white"
            icon="menu"
            class="q-mx-xs"
          />

          <q-space />
          
          <q-btn flat round dense icon="search" color="white" class="q-mr-xs" />
          <q-btn flat round dense icon="notifications" color="white" class="q-mr-xs">
            <q-badge color="red" text-color="white" floating> 2 </q-badge>
          </q-btn>
          <q-btn flat round dense icon="group_add" color="white" @click="logoutUser" />

        </q-toolbar>

        <div class="q-px-lg q-pt-xs q-mb-md" v-if="$q.platform.is.mobile">
            <div class="text-h6 text-white"> {{title}} </div>
        </div>
        <q-img v-if="$q.platform.is.mobile" :src="imgSource" class="header-image absolute-top" />
      </div>
    </q-header>

    <q-header elevated class="bg-white rounded-borders" height-hint="64" v-else-if="$q.platform.is.desktop">
      <div v-if="!$route.fullPath.includes('/auth')">
        <q-toolbar class="GPL__toolbar" style="height: 64px">
          <q-btn
            flat
            dense
            round
            @click="leftDrawerOpen = !leftDrawerOpen"
            aria-label="Menu"
            color="grey"
            icon="menu"
            class="q-mx-xs"
          />

          <q-toolbar-title v-if="$q.screen.gt.sm" shrink class="row items-center no-wrap">
            <img src="https://cdn.quasar.dev/img/layout-gallery/logo-google.svg">
            <span class="q-ml-sm">Photos</span>
          </q-toolbar-title>

          <q-space />

          <q-input class="GPL__toolbar-input" dense standout="bg-primary" v-model="search" placeholder="Search">
            <template v-slot:prepend>
              <q-icon v-if="search === ''" name="search" />
              <q-icon v-else name="clear" class="cursor-pointer" @click="search = ''" />
            </template>
          </q-input>

          <q-space />

          <q-btn flat round dense icon="search" color="grey" class="q-mr-xs" />
          <q-btn flat round dense icon="notifications" color="grey" class="q-mr-xs">
            <q-badge color="red" text-color="white" floating> 2 </q-badge>
          </q-btn>
          <q-btn flat round dense icon="group_add" color="grey" @click="logoutUser" />    

        </q-toolbar>
      </div>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      bordered
      behavior="mobile"
      @click="leftDrawerOpen = false"
      v-if="!$route.fullPath.includes('/auth')"
    >
      <q-scroll-area class="fit">
        <q-toolbar class="GPL__toolbar">
          <q-toolbar-title class="row items-center text-grey-8">
            <img class="q-pl-sm" src="logo1.png" style="height: 160px; max-width: 180px">
            <!-- <span class="q-ml-sm">Photos</span> -->
          </q-toolbar-title>
        </q-toolbar>

        <q-list padding>
          <q-item v-for="link in links1" :key="link.text" clickable :to="link.to" class="GPL__drawer-item">
            <q-item-section avatar>
              <q-icon :name="link.icon" />
            </q-item-section>
            <q-item-section>
              <q-item-label>{{ link.text }}</q-item-label>
            </q-item-section>
          </q-item>

          <q-separator class="q-my-md" />

          <q-item v-for="link in links2" :key="link.text" clickable class="GPL__drawer-item">
            <q-item-section avatar>
              <q-icon :name="link.icon" />
            </q-item-section>
            <q-item-section>
              <q-item-label>{{ link.text }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container class="GPL__page-container">
      <router-view />

      <q-page-sticky v-if="$q.screen.gt.sm && !$route.fullPath.includes('/auth')" expand position="left">
        <div class="fit q-pt-xl q-px-sm column">
          <q-btn round flat color="grey-8" stack no-caps size="26px" class="GPL__side-btn" to="/">
            <q-icon size="22px" name="photo" />
            <div class="GPL__side-btn__label">Dashboard</div>
          </q-btn>

          <q-btn round flat color="grey-8" stack no-caps size="26px" class="GPL__side-btn" to="/commmodity-list">
            <q-icon size="22px" name="import_contacts" />
            <div class="GPL__side-btn__label">Commodity</div>
          </q-btn>

          <q-btn round flat color="grey-8" stack no-caps size="26px" class="GPL__side-btn" to="/commmodity-bid">
            <q-icon size="22px" name="collections_bookmark" />
            <div class="GPL__side-btn__label">Bidding</div>
            <q-badge floating color="red" text-color="white" style="top: 8px; right: 16px">
              1
            </q-badge>
          </q-btn>

          <q-btn round flat color="grey-8" stack no-caps size="26px" class="GPL__side-btn" to="/live-auction">
            <q-icon size="22px" name="assistant" />
            <div class="GPL__side-btn__label">Live Auction</div>
          </q-btn>

          <q-btn round flat color="grey-8" stack no-caps size="26px" class="GPL__side-btn">
            <q-icon size="22px" name="group" />
            <div class="GPL__side-btn__label"> Price Details </div>
          </q-btn>

          <q-btn round flat color="grey-8" stack no-caps size="26px" class="GPL__side-btn" to="/extra">
            <q-icon size="22px" name="import_contacts" />
            <div class="GPL__side-btn__label">Performance</div>
          </q-btn>
        </div>
      </q-page-sticky>
    </q-page-container>
  </q-layout>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'GooglePhotosLayout',
  data () {
    return {
      leftDrawerOpen: false,
      search: '',
      storage: 0.26,
      links1: [
        { icon: 'dashboard', text: 'Dashboard', to: '/' },
        { icon: 'assistant', text: 'Market', to: '/market-dashboard' },
        { icon: 'face', text: 'Profile', to: '/profile' }
      ],
      links2: [
        { icon: 'settings', text: 'Settings' },
        { icon: 'help', text: 'Help & Feedback' },
        { icon: 'logout', text: 'Logout' }
      ]
    }
  },
  computed: {
    title() {
      let currentPath = this.$route.fullPath
      if (currentPath == '/seller-dashboard') return 'My Listings'
      else if (currentPath.includes('/seller-commodity')) return 'Commodity'
      else if (currentPath.includes('/market-dashboard')) return 'Market'
      else if (currentPath.includes('/market-commodity')) return 'Commodity'
      else if (currentPath.includes('/buyer-dashboard')) return 'My Biddings'
      else if (currentPath.includes('/buyer-commodity')) return 'Commodity'
      else if (currentPath.includes('/profile')) return 'My Profile'
      else if (currentPath.includes('/transporter-dashboard')) return 'My Assignments'
      else if (currentPath.includes('/transporter-commodity')) return 'Commodity'

    },
    imgSource() {
      let currentPath = this.$route.fullPath
      if (currentPath == '/seller-dashboard') return 'farmer3.jpg'
      else if (currentPath.includes('/seller-commodity')) return 'farmer3.jpg'
      else if (currentPath.includes('/market-dashboard')) return 'market1.jpg'
      else if (currentPath.includes('/market-commodity')) return 'market1.jpg'
      else if (currentPath.includes('/buyer-dashboard')) return 'buyer1.jpg'
      else if (currentPath.includes('/buyer-commodity')) return 'buyer1.jpg'
      else if (currentPath.includes('/profile')) return 'farmer1.jpg'
      else if (currentPath.includes('/transporter-dashboard')) return 'transporter1.jpg'
      else if (currentPath.includes('/transporter-commodity')) return 'https://www.cateringinsight.com/wp-content/uploads/2016/01/18278-Keith%20Elkington%20Transport%20Fleet%202%20crop.jpg'


    }
  },
  methods: {
    ...mapActions('store', ['logoutUser'])
  }
}
</script>

<style lang="sass">
.GPL
  &__toolbar
    height: 64px
  &__toolbar-input
    width: 35%
  &__drawer-item
    line-height: 24px
    border-radius: 0 24px 24px 0
    margin-right: 12px
    .q-item__section--avatar
      padding-left: 12px
      .q-icon
        color: #5f6368
    .q-item__label:not(.q-item__label--caption)
      color: #3c4043
      letter-spacing: .01785714em
      font-size: .875rem
      font-weight: 500
      line-height: 1.25rem
    &--storage
      border-radius: 0
      margin-right: 0
      padding-top: 24px
      padding-bottom: 24px
  &__side-btn
    &__label
      font-size: 12px
      line-height: 24px
      letter-spacing: .01785714em
      font-weight: 500
  @media (min-width: 1024px)
    &__page-container
      padding-left: 94px
</style>


<style lang="scss">

  .header-image {
    height: 100%;
    z-index: -1;
    opacity: 0.4;
    // filter: grayscale(40%)
  }
</style>