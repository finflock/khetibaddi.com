<template>
    <div>

        <q-card class="my-card q-pa-xs" flat bordered>
            <q-card-section horizontal>
                <q-card-section class="q-pt-xs">
                <div class="text-h5 q-mt-sm q-mb-xs" lines="1"> {{commodity_detail.name}} </div>
                <div class="text-overline text-capitalize text-orange-9"> {{user_info.full_name}} </div>
                <q-rating size="xs" value="3.5" :max="5" color="primary" icon-half="star_half"/>  
                <div class="text-caption text-grey q-py-sm">
                    <div> {{user_address.district}} </div>
                    <div> {{user_address.state}} </div>
                </div>
                </q-card-section>

                <q-space></q-space>

                <q-card-section class="col-5 flex flex-center">
                <q-img
                    class="rounded-borders"
                    :src="commodityImage"
                />
                </q-card-section>
            </q-card-section>

            <!-- <q-separator /> -->

            <q-card-actions>
                <q-badge :class="commodity_detail.status == 'Open' ? 'q-mt-xs q-px-sm q-py-sm text-positive' : 'q-mt-xs q-px-sm q-py-sm text-red-12'" :color="commodity_detail.status == 'Open' ? 'green-1' : 'red-1'">
                    <span class="text-uppercase text-bold"> {{commodity_detail.status}} </span>
                </q-badge>
                <span class="on-right text-grey-8 text-caption text-weight-medium">
                    <span v-if="commodity_detail.status == 'Open'"> till </span>
                    <span v-else> on </span>
                    {{commodity_detail.auction | moment("MMM D , hh:mm a") }}
                </span>
                <q-space></q-space>
        
                <q-btn dense flat color="primary" @click="prompt = true"> Bid now </q-btn>
            </q-card-actions>


            <q-card-section>
          <div class="row no-wrap items-center">
            <div class="col">
              <q-list>
                <q-item>
                  <q-item-section>
                    <q-item-label class="text-grey-8 text-weight-medium"> ₹ {{commodity_detail.base_price}} </q-item-label>
                  </q-item-section>

                  <q-item-section side >
                    <q-item-label caption> Base price </q-item-label>
                  </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                  <q-item-section>
                    <q-item-label class="text-grey-8 text-weight-medium"> ₹ {{commodity_detail.average_bid_price}} </q-item-label>
                  </q-item-section>

                  <q-item-section side >
                    <q-item-label caption> Avg. bid </q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>

            </div>

            <div class="col">
              <q-list>
                <q-item>
                  <q-item-section>
                    <q-item-label class="text-grey-8 text-weight-medium"> {{commodity_detail.quantity}} </q-item-label>
                  </q-item-section>

                  <q-item-section side >
                    <q-item-label caption> Quintal </q-item-label>
                  </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                  <q-item-section>
                    <q-item-label class="text-grey-8 text-weight-medium"> ₹ {{biddings[biddings.length-1].bid_price}} </q-item-label>
                  </q-item-section>

                  <q-item-section side >
                    <q-item-label caption> Last bid </q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>
            </div>
          </div>

        </q-card-section>

        <q-card-section class="bg-yellow-1 text-yellow-9 q-py-sm q-mt-xs">
            <div class="text-subtitle2">
                    <span class="on-right vertical-middle text-uppercase"> All Bids </span>
            </div>
        </q-card-section>

        <q-card-section v-if="biddings.length != 0">
            <q-list class="q-pa-none q-mt-none">
                <div v-for="bidding in biddings" :key="bidding.id">  
                    <q-item>
                        <q-item-section>
                        <q-item-label class="text-weight-medium text-grey-8" lines="1"> {{bidding.buyer_name}} </q-item-label>
                        <div class="row no-wrap items-center">
                            <q-rating size="18px" value="3.5" :max="5" color="red-12" icon-half="star_half"/>
                            <span class="text-caption text-grey q-ml-sm"> 3.5 (45)</span>
                        </div>
                        </q-item-section>

                        <q-item-section side top>
                        <q-badge class="q-pa-sm" color="light-blue-1"> <span class="text-bold text-light-blue"> ₹ {{bidding.bid_price}} </span> </q-badge>
                        </q-item-section>
                    </q-item>

                    <q-separator spaced inset />
                </div>
            </q-list>
        </q-card-section>
        <q-card-section v-else>
            <q-item-label class="q-mb-md"> 
                <q-icon class="text-yellow-9 on-left" style="font-size: 1.5rem;" name="warning"> </q-icon>
                <span class="text-grey-8 text-overline"> No records to show. </span>
            </q-item-label>
        </q-card-section>

        </q-card>

        <q-dialog v-model="prompt" persistent>
            <q-card style="min-width: 250px">
                <q-card-section>
                <div class="text-h6">Your bid</div>
                </q-card-section>

                <q-card-section class="q-pt-none">
                <q-input dense v-model="address" autofocus @keyup.enter="prompt = false" >
                    <template v-slot:prepend>
                        <span class="on-left"> ₹ </span>
                    </template>
                </q-input>
                </q-card-section>

                <q-card-actions align="right" class="text-primary">
                <q-btn flat label="Cancel" v-close-popup />
                <q-btn flat label="Place bid" v-close-popup />
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
            commodity_detail: {},
            biddings: [],
            user_info: {},
            user_address: [],

            prompt: false,


        }
    },

    computed: {
        ...mapGetters('store', ['getUserDetails']),
        commodityImage() {
            var x = this.commodity_detail.name.replace(/\s+/g, '-').toLowerCase();
            var url = 'http://www.khetibaddi.com/media/commodity_picture/' + x + '.jpg'
            return url
        }
    },

    methods: {
        getCommodityDetail() {
            axios.get(this.api_url + 'commodity-detail/' + this.$route.params.commmodityId + '/')
            .then(response => {
                this.commodity_detail = response.data;
                this.getUser()
                })
            .catch(e => {
                this.commodity_detail = {};
            })
        },

        getBidDetail() {
            axios.get(this.api_url + 'bid-detail/?commodity_detail=' + this.$route.params.commmodityId )
            .then(response => {
                this.biddings = response.data.results;
                })
            .catch(e => {
                this.biddings = {};
            })
        },

        getUser() {
            axios.get(this.api_url + 'users/' + this.commodity_detail.user + '/' )
            .then(response => {
                this.user_info = response.data;
                this.getAddress()
                })
            .catch(e => {
                this.user_info = {};
            })
        },

        getAddress() {
            axios.get(this.api_url + 'address/?user=' + this.user_info.id )
            .then(response => {
                this.user_address = response.data.results[0];
                })
            .catch(e => {
                this.user_address = {};
            })
        }
    },

    created() {
        this.getCommodityDetail();
        this.getBidDetail();
    }
}
</script>

<style>

</style>
