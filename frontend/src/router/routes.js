
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: '/auth-login', component: () => import('pages/auth/PageLogin.vue') },
      { path: '/auth-register', component: () => import('pages/auth/PageRegister.vue') },

      { path: '/commmodity-list', component: () => import('pages/PageCommodityList.vue') },
      { path: '/commmodity-bid', component: () => import('pages/PageCommodityBid.vue') },
      // { path: '/live-auction', component: () => import('pages/LiveAuction.vue') },
      { path: '/extra', component: () => import('pages/PageExtra.vue') },
      // { path: '/seller-commodity/:commmodityId', component: () => import('pages/PageSellerCommodity.vue') },
      { path: '/profile/', component: () => import('pages/Profiles/SellerProfile.vue') },

      { path: '/seller-dashboard/', component: () => import('pages/seller/SellerDashboard.vue') },
      { path: '/seller-commodity/:commmodityId', component: () => import('pages/seller/SellerCommodity.vue') },

      { path: '/buyer-dashboard/', component: () => import('pages/buyer/BuyerDashboard.vue') },
      { path: '/buyer-commodity/:commmodityId', component: () => import('pages/buyer/BuyerCommodity.vue') },

      { path: '/transporter-dashboard/', component: () => import('pages/transporter/TransporterDashboard.vue') },
      { path: '/transporter-commodity/:commmodityId', component: () => import('pages/transporter/TransporterCommodity.vue') },

      { path: '/market-dashboard/', component: () => import('pages/market/MarketDashboard.vue') },
      { path: '/market-commodity/:commmodityId', component: () => import('pages/market/MarketCommodity.vue') },

    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
