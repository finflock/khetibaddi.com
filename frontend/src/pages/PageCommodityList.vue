<template>
  <div class="q-pa-md" >
    <div class="row no-wrap items-start">
        <div class="col-auto">
            <q-list>
                <div class="text-h6 ellipsis"> Fruits </div>
                <q-separator spaced inset />
                <q-item v-for="fruit in commodity_details.FRUITS" :key="fruit.id">
                    <q-item-section>
                    <q-item-label> {{fruit}} </q-item-label>
                    </q-item-section>
                </q-item>
            </q-list>
        </div>

        <div class="col-auto">
            <q-list>
                <div class="text-h6 ellipsis"> Vegetables </div>
                <q-separator spaced inset />
                <q-item v-for="fruit in commodity_details.VEGETABLES" :key="fruit.id">
                    <q-item-section>
                    <q-item-label> {{fruit}} </q-item-label>
                    </q-item-section>
                </q-item>
            </q-list>
        </div>

        <div class="col-auto">
            <q-list>
                <div class="text-h6 ellipsis"> Oilseeds </div>
                <q-separator spaced inset />
                <q-item v-for="fruit in commodity_details.OILSEEDS" :key="fruit.id">
                    <q-item-section>
                    <q-item-label> {{fruit}} </q-item-label>
                    </q-item-section>
                </q-item>
            </q-list>
        </div>

        <div class="col-auto">
            <q-list>
                <div class="text-h6 ellipsis"> Spices </div>
                <q-separator spaced inset />
                <q-item v-for="fruit in commodity_details.SPICES" :key="fruit.id">
                    <q-item-section>
                    <q-item-label> {{fruit}} </q-item-label>
                    </q-item-section>
                </q-item>
            </q-list>
        </div>

        <div class="col-auto">
            <q-list>
                <div class="text-h6 ellipsis"> Miscellaneous </div>
                <q-separator spaced inset />
                <q-item v-for="fruit in commodity_details.MISC" :key="fruit.id">
                    <q-item-section>
                    <q-item-label> {{fruit}} </q-item-label>
                    </q-item-section>
                </q-item>
            </q-list>
        </div>

        <div class="col-auto">
            <q-list>
                <div class="text-h6 ellipsis"> Food Grains & Cereals </div>
                <q-separator spaced inset />
                <q-item v-for="fruit in commodity_details.FOOD_GRAINS_CEREALS" :key="fruit.id">
                    <q-item-section>
                    <q-item-label> {{fruit}} </q-item-label>
                    </q-item-section>
                </q-item>
            </q-list>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            commodity_details: {}
        }
    },

    created() {
        this.getCommodityList();
    },

    methods: {
        getCommodityList() {
            axios.get('http://www.khetibaddi.com/api/v1/get-commodity-list/')
            .then(response => {
                this.commodity_details = response.data
                })
            .catch(e => {
                this.commodity_details = {};
            })
        }
    }
}
</script>

<style>

</style>
