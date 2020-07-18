<template>
  <div>
    <div class="q-pa-md row items-start q-gutter-md">
      <q-card class="my-card" flat v-for="comodity in comodity_details" :key="comodity.id">
        <q-img
          style="height: 200px;"
          :src="comodity.image"
        />

        <q-card-section>
          <q-btn
            fab
            color="primary"
            icon="place"
            class="absolute"
            style="top: 0; right: 12px; transform: translateY(-50%);"
          />

          <div class="row no-wrap items-center">
            <div class="col text-h6 ellipsis">
              {{comodity.name}}
            </div>

          </div>

          
        </q-card-section>

        <q-separator  inset />

        <q-card-section>
          <div class="row no-wrap items-center">
            <div class="col">
              <q-list>
                <q-item>
                  <q-item-section>
                    <q-item-label class="text-weight-bold"> ₹ {{comodity.bid_base_price}} </q-item-label>
                  </q-item-section>

                  <q-item-section side >
                    <q-item-label caption> Base price </q-item-label>
                  </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                  <q-item-section>
                    <q-item-label class="text-weight-bold"> ₹ {{comodity.bid_avg_price}} </q-item-label>
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
                    <q-item-label class="text-weight-bold"> {{comodity.total_quantity}} Kg </q-item-label>
                  </q-item-section>

                  <q-item-section side >
                    <q-item-label caption> Quantity </q-item-label>
                  </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                  <q-item-section>
                    <q-item-label class="text-weight-bold"> ₹ {{comodity.bid_last_price}} </q-item-label>
                  </q-item-section>

                  <q-item-section side >
                    <q-item-label caption> Last bid </q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>
            </div>
          </div>

        </q-card-section>

        <q-card-actions>
          <q-space />
          <div class="q-gutter-md row items-start">
            <q-input class="col" outlined v-model="comodity.bid_price_input" label="Bid amount" dense >
              <template v-slot:prepend>
                ₹
              </template>
            </q-input>

            <q-input class="col" outlined v-model="comodity.bid_quantity_input" label="Quantity (Kg)" dense >
              <template v-slot:prepend>
                ₹
              </template>
            </q-input>
          </div>


          <div class="text-overline text-gray q-ml-sm"> {{comodity.total_bids}} bids so far </div>
          <q-btn
            color="grey"
            round
            label="as"
            flat
            dense
            :icon="expanded ? 'keyboard_arrow_up' : 'keyboard_arrow_down'"
            @click="expanded = !expanded"
          />
          <q-space />
          <q-btn flat color="primary" label="Place your bid" />
          

        </q-card-actions>

        <q-slide-transition>
          <div v-show="expanded">
            <q-separator />
            <q-card-section class="text-subitle2">
              {{ lorem }}
            </q-card-section>
          </div>
        </q-slide-transition>

        <q-separator spaced inset />

        <q-card-actions >
          <q-btn flat round icon="event" />
          <q-btn flat>
            Ends {{comodity.end_date}}
          </q-btn>
          <q-space />
          <q-btn flat round color="red" icon="favorite" />
          <q-btn flat round color="teal" icon="bookmark" />
          <q-btn flat round color="primary" icon="share" />
        </q-card-actions>
      </q-card>
    </div>

    <q-page-sticky position="bottom-right" :offset="[40, 40]">
            <q-fab
              icon="add"
              direction="left"
              color="accent"
            >
              <q-fab-action  @click="prompt = true" color="primary" icon="person_add" />
              <q-fab-action @click="onClick" color="primary" icon="mail" />
            </q-fab>
          </q-page-sticky>

        <q-dialog v-model="prompt" persistent>
            <q-card style="min-width: 350px">
                <q-card-section>
                <div class="text-h6">Enter details</div>
                </q-card-section>

                <q-card-section class="q-pt-none">
                <q-input label="Select commodity" v-model="address" autofocus @keyup.enter="prompt = false" />
                <q-input label="Enter base price" v-model="address" @keyup.enter="prompt = false" />
                <q-input label="Enter total quantity" v-model="address" @keyup.enter="prompt = false" />
                <q-input label="Enter total quantity" v-model="address" @keyup.enter="prompt = false" />

                </q-card-section>

                <q-card-actions align="right" class="text-primary">
                <q-btn flat label="Cancel" v-close-popup />
                <q-btn flat label="Add" v-close-popup />
                </q-card-actions>
            </q-card>
        </q-dialog>

  </div>
</template>


<script>
export default {
  data () {
    return {
      prompt: false,

      expanded: false,
      slide: 'style',
      lorem: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      comodity_details: [{
        name: 'Red Chilli',
        image: 'https://i.ndtvimg.com/i/2015-02/chilli-625_625x350_41423486929.jpg',
        distance: '2.5 km',
        farmer_name: 'Inderjit Singh',
        farmer_location: 'Amritsar, Punjab',
        farmer_rating: '3.5',
        farmer_reviews: '251',
        bid_base_price: 170,
        total_quantity: 30,
        bid_avg_price: 175,
        bid_last_price: 178,
        bid_price_input: null,
        bid_quantity_input: null,
        total_bids: 16,
        end_date: 'JULY 16'
      },
      {
        name: ' Buck Wheat',
        image: 'https://cdn-prod.medicalnewstoday.com/content/images/articles/325/325042/dried-buckwheat-grains-on-a-wooden-spoon.jpg',
        distance: '6.5 km',
        farmer_name: 'Sunil Sharma',
        farmer_location: 'Noida, Uttar Pradesh',
        farmer_rating: '3.8',
        farmer_reviews: '86',
        bid_base_price: 249,
        total_quantity: 60,
        bid_avg_price: 260,
        bid_last_price: 262,
        bid_price_input: null,
        bid_quantity_input: null,
        total_bids: 23,
        end_date: 'JULY 20'
      },
      {
        name: 'Apples',
        image: 'https://www.promessedefleurs.com/media/catalog/product/cache/1/image/820x/9df78eab33525d08d6e5fb8d27136e95/P/o/Pommier-Delbarestivale-Georges-Delbard-84757-1.jpg',
        distance: '9 km',
        farmer_name: 'Harpreet Singh',
        farmer_location: 'Amritsar, Punjab',
        farmer_rating: '4.2',
        farmer_reviews: '79',
        bid_base_price: 125,
        total_quantity: 35,
        bid_avg_price: 136,
        bid_last_price: 140,
        bid_price_input: null,
        bid_quantity_input: null,
        total_bids: 12,
        end_date: 'JULY 15'
      },
      {
        name: 'Coconut',
        image: 'https://i.unu.edu/media/ourworld.unu.edu-en/article/4538/Videobriefs-19.jpg',
        distance: '5.3 km',
        farmer_name: 'Sharad Pawar',
        farmer_location: 'Pune, Maharashtra',
        farmer_rating: '3.9',
        farmer_reviews: '45',
        bid_base_price: 90,
        total_quantity: 15,
        bid_avg_price: 100,
        bid_last_price: 102,
        bid_price_input: null,
        bid_quantity_input: null,
        total_bids: 6,
        end_date: 'JULY 20'
      },
      {
        name: 'Coriander Leaves',
        image: 'https://images.indianexpress.com/2018/02/corainder-759-thinkstock.jpg',
        distance: '5.3 km',
        farmer_name: 'Ketan Farma',
        farmer_location: 'Pune, Maharashtra',
        farmer_rating: '4.5',
        farmer_reviews: '111',
        bid_base_price: 70,
        total_quantity: 50,
        bid_avg_price: 76,
        bid_last_price: 79,
        bid_price_input: null,
        bid_quantity_input: null,
        total_bids: 19,
        end_date: 'JULY 18'
      }]
    }
  }
}
</script>


<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 340px
</style>