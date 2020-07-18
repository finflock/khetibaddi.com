<template>
  <div class="q-pa-sm q-mt-xs">
    <q-list v-if="listings.length != 0">
      <div v-for="listing in listings" :key="listing.id">
        <q-item clickable v-ripple :to="'/market-commodity/' + listing.id">
          <q-item-section>
            <q-item-label class="text-bold text-brown-9" lines="1"> {{listing.name}} </q-item-label>
            <q-item-label caption lines="1" class="text-bold"> {{listing.bid_count}} bids</q-item-label>
            <q-item-label caption lines="1"> <span class="text-weight-medium"> {{listing.created | moment("MMM D , hh:mm") }} </span> </q-item-label>
          </q-item-section>

          <q-item-section side bottom class="q-mt-sm">
            <q-item-label caption> <span class="text-bold text-light-blue-7"> ₹ {{listing.base_price}} /- </span> <span class="text-bold text-grey-7">for {{listing.quantity}} Quintals </span> </q-item-label>
            <q-badge :class="listing.status == 'Open' ? 'q-mt-sm q-px-sm q-py-xs text-positive' : 'q-mt-sm q-px-sm q-py-xs text-red-12'" :color="listing.status == 'Open' ? 'green-1' : 'red-1'">
              <span class="q-ml-xs text-weight-medium"> {{listing.auction | moment("MMM D , hh:mm") }} </span>
            </q-badge>
          </q-item-section>
        </q-item>
        <q-separator spaced inset />
      </div>
    </q-list>

    <div v-else>
        <q-icon class="text-yellow-9 on-left" style="font-size: 1.5rem;" name="warning"> </q-icon>
        <span class="text-overline text-grey-8"> No records to show. </span>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex'

export default {
  data() {
    return {

      api_url: "http://www.khetibaddi.com/api/v1/",
      user_basic_info: [],
      listings: [],

      

    }
  },

  computed: {
      ...mapGetters('store', ['getUserDetails'])
  },

  methods: {
    getUserBasicInfo() {
        axios.get(this.api_url + 'users/?email=' + this.getUserDetails.email)
        .then(response => {
            this.user_basic_info = response.data.results[0]
            this.getListings()

            })
        .catch(e => {
            this.user_basic_info = [];
        })
    },


    getListings() {
      axios.get(this.api_url + 'commodity-detail/?status=Open')
      .then(response => {
          this.listings = response.data.results
          })
      .catch(e => {
          this.listings = [];
      })
    },

  },

  created() {
    this.getUserBasicInfo()
  }
}
</script>
