<template>
  <div class="q-pa-sm q-mt-xs">
    <q-list>
      <div v-for="listing in listings" :key="listing.id">
        <q-item clickable v-ripple :to="'/seller-commodity/' + listing.id">
          <q-item-section>
            <q-item-label class="text-bold text-brown-9" lines="1"> {{listing.commodity_name}} </q-item-label>
            <q-item-label caption lines="1" class="text-bold"> {{listing.total_bids}} bids</q-item-label>
            <q-item-label caption lines="1"> <span class="text-"> {{listing.created}} </span> </q-item-label>
          </q-item-section>

          <q-item-section side bottom class="q-mt-sm">
            <q-item-label caption> <span class="text-bold text-light-blue-7"> ₹ {{listing.base_price}} </span> <span class="text-bold text-grey-7">for {{listing.quintals}} Quintal </span> </q-item-label>
            <q-badge :class="listing.status == 'Open' ? 'q-mt-sm q-px-sm q-py-xs text-positive' : 'q-mt-sm q-px-sm q-py-xs text-red-12'" :color="listing.status == 'Open' ? 'green-1' : 'red-1'">
              <span class="text-uppercase text-bold"> {{listing.status}} </span> <span class="q-ml-xs text-bold"> - {{listing.expiry}} </span>
            </q-badge>
          </q-item-section>
        </q-item>
        <q-separator spaced inset />
      </div>
    </q-list>

    <q-page-sticky position="bottom-right" :offset="[15, 15]">
      <q-btn round color="brown-7" icon="add" @click="showAddCommodity = true"> </q-btn>
    </q-page-sticky>

    <q-dialog v-model="showAddCommodity">
		  <q-card class="q-pa-xs" style="min-width: 300px">
        <q-card-section>
          <div class="text-h6"> List a commodity </div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input dense class="q-py-xs" filled v-model="formData.commodity_category" label="Commodity category"> </q-input>
          <q-input dense class="q-py-xs" filled v-model="formData.commodity_name" label="Commodity"> </q-input>
          <q-input dense class="q-py-xs" filled v-model="formData.base_price" label="Base price (per quintal)"> </q-input>
          <q-input dense class="q-py-xs" filled v-model="formData.quantity" label="Total quantity (in quintal)"> </q-input>
          <q-input dense class="q-py-xs" filled v-model="formData.end_datetime" label="End date"> </q-input>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup />
          <q-btn color="primary" label="Post" v-close-popup />
        </q-card-actions>
      </q-card>
		</q-dialog>
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

      showAddCommodity: false,

      listings: [{
        id: 1,
        commodity_name: "Red Chilli",
        base_price: '170,000/-',
        quintals: 10,
        total_bids: 7,
        created: "Mon, 13 July",
        expiry: "6 days left",
        status: "Open"
      },
      {
        id: 2,
        commodity_name: "Buck Wheat",
        base_price: '250,000/-',
        quintals: 6,
        total_bids: 10,
        created: "Mon, 14 July",
        expiry: "13 days left",
        status: "Open"
      },
      {
        id: 3,
        commodity_name: "Apples",
        base_price: '125,000/-',
        quintals: 10,
        total_bids: 11,
        created: "Mon, 14 July",
        expiry: "5 days left",
        status: "Open"
      },
      {
        id: 4,
        commodity_name: "Coconut",
        base_price: '90,000/-',
        quintals: 20,
        total_bids: 18,
        created: "Mon, 8 July",
        expiry: "10 days ago",
        status: "Closed"
      },
      {
        id: 5,
        commodity_name: "Coriander Leaves",
        base_price: '70,000/-',
        quintals: 20,
        total_bids: 18,
        created: "Mon, 4 July",
        expiry: "10 days ago",
        status: "Closed"
      }],

      formData: {
        commodity_category: null,
        commodity_name: null,
        base_price: null,
        quantity: null,
        end_datetime: null

      }
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
      axios.get(this.api_url + 'commodity-detail/?user=' + this.user_basic_info.id)
      .then(response => {
          this.listings = response.data.results
          })
      .catch(e => {
          this.listings = [];
      })
    },


    postListings() {
      const params = new URLSearchParams();
      params.append('quality', 'Good');
      params.append('quantity', this.formData.quantity);
      params.append('expected_price', this.formData.base_price);
      params.append('auction', this.formData.end_datetime);
      params.append('grain_name', this.formData.commodity_name);
      params.append('user', this.user_basic_info.id);
      params.append('active', true);

      axios.post(this.api_url+'users/', params)
          .then(response => {
              console.log("Item Listed")
          })
          .catch(e => {
              console.log("Error while listing")              
          });
    }
  },

  created() {
    // this.getUserBasicInfo()
  }
}
</script>
