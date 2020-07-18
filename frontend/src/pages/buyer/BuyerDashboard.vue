<template>
  <div class="q-pa-sm q-mt-xs">
    <q-list>
      <div v-for="bidding in biddings" :key="bidding.id">
        <q-item clickable v-ripple :to="'/buyer-commodity/' + bidding.commodity_detail">
          <q-item-section>
            <q-item-label class="text-bold text-brown-9" lines="1"> {{bidding.commodity_name}} </q-item-label>
            <q-item-label caption lines="1" class="text-weight-medium"> Placed on </q-item-label>
            <q-item-label caption lines="1"> <span class="text-weight-medium"> {{bidding.created | moment("MMM D , hh:mm") }} </span> </q-item-label>
          </q-item-section>

          <q-item-section side bottom class="q-mt-sm">
            <q-item-label caption> <span class="text-bold text-light-blue-7"> ₹ {{bidding.bid_price}}/- </span> <span class="text-bold text-grey-7">for {{bidding.quantity}} Quintal </span> </q-item-label>
            <q-badge :class="bidding.accept_bid == true ? 'q-mt-sm q-px-sm q-py-xs text-positive' : 'q-mt-sm q-px-sm q-py-xs text-red-12'" :color="bidding.accept_bid == true ? 'green-1' : 'red-1'">
              <span v-if="bidding.accept_bid == true" class="text-uppercase text-bold"> Bid Accepted </span>
              <span v-else class="text-uppercase text-bold"> Bid Lost </span>
            </q-badge>
          </q-item-section>
        </q-item>
        <q-separator spaced inset />
      </div>
    </q-list>
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
      biddings:[],

      

      user_basic_info: []

      
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
            this.getBidDetail();
            })
        .catch(e => {
            this.user_basic_info = [];
        })
    },

    getBidDetail() {
        axios.get(this.api_url + 'bid-detail/?user=' + this.user_basic_info.id )
        .then(response => {
            this.biddings = response.data.results;
            })
        .catch(e => {
            this.biddings = {};
        })
    },

  },

  created() {
    this.getUserBasicInfo();
  }
}
</script>
