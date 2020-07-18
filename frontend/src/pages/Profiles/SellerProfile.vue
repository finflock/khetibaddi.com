<template>
    <div>
        <q-form>
            <div class="q-gutter-md q-pa-md">
                <div>
                    <!-- <q-input dense filled  type="text" external-label label-position="top" prefix="Full name:">
                        <template v-slot:prepend>
                            <q-icon name="person" class="q-mr-xs" />
                        </template>
                    </q-input> -->

                    <q-card flat class="my-card">

                        <q-card-section>
                            <q-item class="q-pl-none">
                                <q-item-section top avatar>
                                <q-avatar color="secondary" text-color="white">
                                    <span class="text-uppercase"> {{user_basic_info.full_name.charAt(0)}} </span>
                                </q-avatar>
                                </q-item-section>

                                <q-item-section>
                                <q-item-label class="text-weight-medium"> {{user_basic_info.full_name}} </q-item-label>
                                <q-item-label caption>
                                    <div class="q-py-xs"> {{getUserDetails.user_type}} </div>
                                    <q-rating size="18px" value="3.5" :max="5" color="red-12" icon-half="star_half"/>
                                    <span class="text-caption text-grey-8 q-ml-sm"> 3.5 (79)</span>
                                </q-item-label>
                                </q-item-section>
                            </q-item>
                        </q-card-section>

                         <!-- #########################  Basic Info ######################### -->

                        <q-card-section class="bg-cyan-1 text-light-blue q-py-sm q-mt-xs">
                            <div class="text-subtitle2">
                                 <span class="on-right vertical-middle text-uppercase"> Basic Information </span>
                                 <q-btn class="float-right" color="light-blue" size="xs" square  text-color="white" @click="onClick" icon="edit"/>
                            </div>
                        </q-card-section>
                        <q-card-section class="bg-white text-grey">
                            <q-item-label caption class="q-py-xs" lines="1">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name="person"> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle"> {{user_basic_info.gender}} </span>
                            </q-item-label>
                            <q-item-label caption class="q-py-xs" lines="1">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name="call"> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle"> +91 - {{user_basic_info.mobile}} </span>
                            </q-item-label>
                            <q-item-label caption class="q-py-xs" lines="1">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name="email"> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle"> {{user_basic_info.email}} </span>
                            </q-item-label>
                        </q-card-section>


                        <!-- #########################  Address ######################### -->


                        <q-card-section class="bg-red-1 text-red-12 q-py-sm q-mt-xs">
                            <div class="text-subtitle2">
                                 <span class="on-right vertical-middle text-uppercase"> Address </span>
                                 <q-btn class="float-right" color="red-12" size="xs" text-color="white" @click="showUpdateAddress = true" icon="edit"/>
                            </div>
                        </q-card-section>
                        <q-card-section class="bg-white text-grey" v-if="user_address.active">
                            <q-item-label caption class="q-py-xs" lines="2">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name="home"> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle" lines="1"> {{user_address.address_1}} </span>
                            </q-item-label>
                            <q-item-label caption class="q-py-xs" lines="2">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name=""> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle" lines="1"> {{user_address.address_2}} </span>
                            </q-item-label>
                            <q-item-label caption class="q-py-xs" lines="1">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name=""> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle"> {{user_address.district}}, {{user_address.state}} </span>
                            </q-item-label>
                            <q-item-label caption class="q-py-xs" lines="1">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name=""> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle"> Pin Code - {{user_address.pin_code}} </span>
                            </q-item-label>
                        </q-card-section>
                        <q-card-section v-else>
                            <q-item-label class="q-mb-md"> 
                                <q-icon class="text-yellow-9 on-left" style="font-size: 1.5rem;" name="warning"> </q-icon>
                                <span> No records to show. </span>
                            </q-item-label>
                        </q-card-section>


                        <q-dialog v-model="showUpdateAddress">
                            <q-card style="min-width: 300px">
                                <q-card-section>
                                    <div class="text-h6"> Update your Address </div>
                                </q-card-section>

                                <q-card-section class="q-pt-none">
                                    <q-input class="q-py-sm" dense filled v-model="user_address.address_1" label="Address line 1"> </q-input>
                                    <q-input class="q-py-sm" dense filled v-model="user_address.address_2" label="Address line 2 (optional)"> </q-input>
                                    <q-select class="q-py-sm" dense filled v-model="user_address.state"
                                        use-input
                                        hide-selected
                                        fill-input
                                        input-debounce="0"
                                        :options="all_india_states"
                    
                                        @filter="filterFn"
                                        label="Select State"> </q-select>
                                    <q-input class="q-py-sm" dense filled v-model="user_address.district" label="Select District"> </q-input>
                                    <q-input class="q-py-sm" dense filled v-model="user_address.pin_code" label="Pin code"> </q-input>
                                </q-card-section>

                                <q-card-actions align="right" class="text-primary">
                                    <q-btn flat label="Cancel" v-close-popup @click="getAddress" />
                                    <q-btn color="primary" v-close-popup label="Update" @click="putAddress" />
                                </q-card-actions>
                            </q-card>
                        </q-dialog>


                        <!-- #########################  Bank Details ######################### -->


                        <q-card-section class="bg-green-1 text-secondary q-py-sm q-mt-xs">
                            <div class="text-subtitle2">
                                 <span class="on-right vertical-middle text-uppercase"> Bank Details </span>
                                 <q-btn class="float-right" color="secondary" size="xs" text-color="white" @click="showUpdateBank = true" icon="edit"/>
                            </div>
                        </q-card-section>
                        <q-card-section class="bg-white text-grey" v-if="user_bank_details.active">
                            <q-item-label caption class="q-py-xs" lines="2">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name="account_balance"> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle" lines="2"> {{user_bank_details.account_holder_name}} </span>
                            </q-item-label>
                            <q-item-label caption class="q-py-xs" lines="1">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name=""> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle"> Acc. Number -  {{user_bank_details.bank_account_number}} </span>
                            </q-item-label>
                            <q-item-label caption class="q-py-xs" lines="1">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name=""> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle"> IFSC code -  {{user_bank_details.ifsc_code}} </span>
                            </q-item-label>
                        </q-card-section>
                        <q-card-section v-else>
                            <q-item-label class="q-mb-md"> 
                                <q-icon class="text-yellow-9 on-left" style="font-size: 1.5rem;" name="warning"> </q-icon>
                                <span> No records to show. </span>
                            </q-item-label>
                        </q-card-section>

                        <q-dialog v-model="showUpdateBank">
                            <q-card class="q-pa-xs" style="min-width: 300px">
                                <q-card-section>
                                    <div class="text-h6"> Update bank details </div>
                                </q-card-section>

                                <q-card-section class="q-pt-none">
                                    <q-input class="q-py-sm" dense filled v-model="user_bank_details.account_holder_name" label="Account holder name"> </q-input>
                                    <q-input class="q-py-sm" dense filled v-model="user_bank_details.bank_account_number" label="Account number"> </q-input>
                                    <q-input class="q-py-sm" dense filled v-model="user_bank_details.ifsc_code" label="IFSC Code"> </q-input>
                                </q-card-section>

                                <q-card-actions align="right" class="text-primary">
                                    <q-btn flat label="Cancel" v-close-popup @click="getBankDetails" />
                                    <q-btn color="primary" v-close-popup label="Update" @click="putBankDetails" />
                                </q-card-actions>
                            </q-card>
                        </q-dialog>


                        <!-- #########################  Identification ######################### -->


                        <q-card-section class="bg-yellow-1 text-yellow-9 q-py-sm q-mt-xs">
                            <div class="text-subtitle2">
                                 <span class="on-right vertical-middle text-uppercase"> Identification </span>
                                 <q-btn class="float-right" color="yellow-8" size="xs" text-color="white" @click="showUpdateKyc = true" icon="edit"/>
                            </div>
                        </q-card-section>
                        <q-card-section class="bg-white text-grey" v-if="user_kyc_details.active">
                            <q-item-label caption class="q-py-xs" lines="2">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name="fingerprint"> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle" lines="2"> {{user_kyc_details.photo_id_type}} </span>
                            </q-item-label>
                            <q-item-label caption class="q-py-xs" lines="1">
                                <q-icon class="text-light-blue" style="font-size: 1.5rem;"  name=""> </q-icon>
                                <span class="text-bold text-grey-8 q-ml-sm vertical-middle"> {{user_kyc_details.id_number}} </span>
                            </q-item-label>
                        </q-card-section>
                        <q-card-section v-else>
                            <q-item-label class="q-mb-md"> 
                                <q-icon class="text-yellow-9 on-left" style="font-size: 1.5rem;" name="warning"> </q-icon>
                                <span> No records to show. </span>
                            </q-item-label>
                        </q-card-section>


                        <q-dialog v-model="showUpdateKyc">
                            <q-card class="q-pa-xs" style="min-width: 300px">
                                <q-card-section>
                                    <div class="text-h6"> Update your ID </div>
                                </q-card-section>

                                <q-card-section class="q-pt-none">
                                    <q-select class="q-py-sm" dense filled v-model="user_kyc_details.photo_id_type" label="Photo ID Type" :options="['ADHAR CARD', 'PAN CARD', 'VOTER CARD']"> </q-select>
                                    <q-input class="q-py-sm" dense filled v-model="user_kyc_details.id_number" label="Photo ID Number"> </q-input>
                                </q-card-section>

                                <q-card-actions align="right" class="text-primary">
                                    <q-btn flat label="Cancel" v-close-popup @click="getKycDetails" />
                                    <q-btn color="primary" v-close-popup label="Update" @click="putKycDetails" />
                                </q-card-actions>
                            </q-card>
                        </q-dialog>

                    </q-card>
                </div>
            </div>
        </q-form>
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
            user_address: [],
            user_bank_details: [],
            user_kyc_details: [],

            showUpdateAddress: false,
            showUpdateKyc: false,
            showUpdateBank: false,

            all_india_states: ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana',
                                'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
                                'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
                                'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'],
            district_options: []

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
                this.getAddress()
                this.getBankDetails()
                this.getKycDetails()
                })
            .catch(e => {
                this.user_basic_info = [];
            })
        },

        getAddress() {
            axios.get(this.api_url + 'address/?user=' + this.user_basic_info.id)
            .then(response => {
                this.user_address = response.data.results[0]
                })
            .catch(e => {
                this.user_address = [];
            })
        },

        getBankDetails() {
            axios.get(this.api_url + 'bank-detail/?user=' + this.user_basic_info.id)
            .then(response => {
                this.user_bank_details = response.data.results[0]
                })
            .catch(e => {
                this.user_bank_details = [];
            })
        },

        getKycDetails() {
            axios.get(this.api_url + 'kyc-detail/?user=' + this.user_basic_info.id)
            .then(response => {
                this.user_kyc_details = response.data.results[0]
                })
            .catch(e => {
                this.user_kyc_details = [];
            })
        },


        filterFn (val, update, abort) {
        update(() => {
            const needle = val.toLowerCase()
            this.all_india_states = this.all_india_states.filter(v => v.toLowerCase().indexOf(needle) > -1)
        })
        },

        getDistrict() {
            axios.get(this.api_url + 'state-wise-district/?state=' + this.user_address.state)
            .then(response => {
                this.district_options = response.data.results
                })
            .catch(e => {
                this.district_options = [];
            })
        },

        putAddress() {
            this.user_address.active = true
            var data = JSON.stringify(this.user_address);

            var config = {
                method: 'put',
                url: this.api_url+'address/'+this.user_address.id+'/' ,
                headers: { 
                    'Content-Type': 'application/json'
                },
                data : data
            };

            axios(config)
                .then(response => {
                    this.getAddress();
                })
                .catch(e => {
                    // this.user_address = [];
                    console.log("Error while updating address.");
                });
        },


        putKycDetails() {
            this.user_kyc_details.active = true
            var data = JSON.stringify(this.user_kyc_details);

            var config = {
                method: 'put',
                url: this.api_url+'kyc-detail/'+this.user_kyc_details.id+'/' ,
                headers: { 
                    'Content-Type': 'application/json'
                },
                data : data
            };

            axios(config)
                .then(response => {
                    this.getKycDetails();
                })
                .catch(e => {
                    // this.user_address = [];
                    console.log("Error while updating kyc.");
                });
        },


        putBankDetails() {
            this.user_bank_details.active = true
            var data = JSON.stringify(this.user_bank_details);

            var config = {
                method: 'put',
                url: this.api_url+'bank-detail/'+this.user_bank_details.id+'/' ,
                headers: { 
                    'Content-Type': 'application/json'
                },
                data : data
            };

            axios(config)
                .then(response => {
                    this.getBankDetails();
                })
                .catch(e => {
                    // this.user_address = [];
                    console.log("Error while updating bank detailss.");
                });
        }
    },

    created() {
        this.getUserBasicInfo()
    }

}
</script>

<style>

</style>


