<template>
    <div>
        <!-- {{this.$route.params.commmodityId}} -->
        <q-banner dense inline-actions class="text-white bg-light-blue q-pa-md">
            <span class="text-bold"> 7 buyers are bidding on average ₹ 178,000 for your commodity. </span>
        </q-banner>
        
    <q-list class="q-pa-sm q-mt-xs">
      <div v-for="buyer in buyers" :key="buyer.id">  
        <q-item>
            <q-item-section>
            <q-item-label class="text-bold text-grey-8" lines="1"> {{buyer.name}} </q-item-label>
            <div class="row no-wrap items-center">
                <q-rating size="18px" v-model="buyer.rating" :max="5" color="red-12" icon-half="star_half"/>
                <span class="text-caption text-grey q-ml-sm"> {{buyer.rating}} ({{buyer.reviews}})</span>
            </div>
            </q-item-section>

            <q-item-section side top>
            <q-badge class="q-pa-sm" color="light-blue-1"> <span class="text-bold text-light-blue"> ₹ {{buyer.bid}} </span> </q-badge>
            </q-item-section>
        </q-item>

        <q-separator spaced inset />
      </div>
    </q-list>

    <q-page-sticky position="bottom-right" :offset="[15, 15]">
        <q-fab color="red-12" text-color="white" icon="keyboard_arrow_left" direction="left" external-label label-position="top" padding="sm">
            <q-fab-action color="red-12" text-color="white" external-label label-position="top" @click="confirm = true" icon="delete"  label="Delete"/>
            <q-fab-action color="light-blue" text-color="white" external-label label-position="top" @click="onClick" icon="edit" label="Edit"/>
        </q-fab>
    </q-page-sticky>

    <q-dialog v-model="confirm" persistent>
      <q-card style="width: 100%">
        <q-card-section class="row items-center">
          <q-avatar icon="delete" color="primary" text-color="white" />
          <span class="q-ml-sm">Are you sure?</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="grey-9" v-close-popup />
          <q-btn flat label="Delete" color="primary" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>

    </div>
</template>

<script>
export default {
    data() {
        return {
            confirm: false,

            buyers: [{
                id: 1,
                name: 'Hari Sharma',
                rating: 3.5,
                reviews: 251,
                bid: '170,000'
            },
            {
                id: 2,
                name: 'Harpreet Singh',
                rating: 4.2,
                reviews: 112,
                bid: '171,600'
            },
            {
                id: 3,
                name: 'Sunil Mishra',
                rating: 3.1,
                reviews: 72,
                bid: '172,800'
            },
            {
                id: 4,
                name: 'Inderjeet Singh',
                rating: 4.1,
                reviews: 179,
                bid: '174,000'
            },
            {
                id: 5,
                name: 'Prashant Apte',
                rating: 3.9,
                reviews: 44,
                bid: '176,600'
            },
            {
                id: 6,
                name: 'Rahul Sharma',
                rating: 4.4,
                reviews: 204,
                bid: '178,400'
            },
            {
                id: 7,
                name: 'Satpal Singh',
                rating: 4.2,
                reviews: 73,
                bid: '180,000'
            }]
        }
    }
}
</script>

<style>

</style>
