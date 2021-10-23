<template>
  <div>
    <header>
      <!-- Sidebar -->
      <base-sidebar />

      <!-- Navbar -->
      <base-navbar />
    </header>

    <main style="margin-top: 58px">
      <div class="container pt-4">
        <!-- Page header -->
        <page-header :current-page="'Some page'" />

        <!-- Statistic cards -->
        <section id="statistics">
          <div class="row">
            <minimal-stat-card
              v-for="(statistic, index) in statistics"
              :key="index"
              :share-value="statistic.shareValue"
              :color="statistic.color"
              :icon="statistic.icon"
              :title="statistic.title"
              :is-percentage="statistic.isPercentage"
              :value="statistic.value"
            />
          </div>
        </section>

        <section class="mb-4">
          <div class="card">
            <div class="card-header py-3">
              <h5 class="mb-0 text-center">
                <strong>Sales</strong>
              </h5>
            </div>

            <div class="card-body">
              <base-bar-chart
                :chart-data="chartData"
                :options="options"
              />
            </div>
          </div>
        </section>

        <section class="mb-4">
          <div class="card">
            <div class="card-header text-center py-3">
              <h5 class="mb-0 text-center">
                <strong>Sales Performance KPIs</strong>
              </h5>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <table class="table table-hover text-nowrap">
                  <thead>
                    <tr>
                      <th scope="col" />
                      <th scope="col">
                        Product Detail Views
                      </th>
                      <th scope="col">
                        Unique Purchases
                      </th>
                      <th scope="col">
                        Quantity
                      </th>
                      <th scope="col">
                        Product Revenue
                      </th>
                      <th scope="col">
                        Avg. Price
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <th scope="row">
                        Value
                      </th>
                      <td>18,492</td>
                      <td>228</td>
                      <td>350</td>
                      <td>$4,787.64</td>
                      <td>$13.68</td>
                    </tr>
                    <tr>
                      <th scope="row">
                        Percentage change
                      </th>
                      <td>
                        <span class="text-danger">
                          <i class="fas fa-caret-down me-1" /><span>-48.8%%</span>
                        </span>
                      </td>
                      <td>
                        <span class="text-success">
                          <i class="fas fa-caret-up me-1" /><span>14.0%</span>
                        </span>
                      </td>
                      <td>
                        <span class="text-success">
                          <i class="fas fa-caret-up me-1" /><span>46.4%</span>
                        </span>
                      </td>
                      <td>
                        <span class="text-success">
                          <i class="fas fa-caret-up me-1" /><span>29.6%</span>
                        </span>
                      </td>
                      <td>
                        <span class="text-danger">
                          <i class="fas fa-caret-down me-1" /><span>-11.5%</span>
                        </span>
                      </td>
                    </tr>
                    <tr>
                      <th scope="row">
                        Absolute change
                      </th>
                      <td>
                        <span class="text-danger">
                          <i class="fas fa-caret-down me-1" /><span>-17,654</span>
                        </span>
                      </td>
                      <td>
                        <span class="text-success">
                          <i class="fas fa-caret-up me-1" /><span>28</span>
                        </span>
                      </td>
                      <td>
                        <span class="text-success">
                          <i class="fas fa-caret-up me-1" /><span>111</span>
                        </span>
                      </td>
                      <td>
                        <span class="text-success">
                          <i class="fas fa-caret-up me-1" /><span>$1,092.72</span>
                        </span>
                      </td>
                      <td>
                        <span class="text-danger">
                          <i class="fas fa-caret-down me-1" /><span>$-1.78</span>
                        </span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<script>
import BaseNavbar from '../components/dashboard/BaseDashboardNavbar.vue'
import BaseSidebar from '../components/dashboard/BaseSidebar.vue'
import BaseBarChart from '../components/dashboard/charts/BaseBarChart.vue'
import MinimalStatCard from '../components/dashboard/MinimalStatCard.vue'
import PageHeader from '../components/dashboard/PageHeader.vue'

export default {
  name: 'Dashboard',
  components: { BaseSidebar, BaseNavbar, PageHeader, MinimalStatCard, BaseBarChart },
  data() {
    return {
      statistics: [
        { title: 'Comments', value: 45.3, icon: 'pencil-alt', color: 'info', isPercentage: true, shareValue: 4 }, 
        { title: 'Posts', value: 100, icon: 'comment-alt', color: 'warning' }, 
        { title: 'Total visits', value: 100, icon: 'chart-line', color: 'danger' }, 
        { title: 'Bounce rates', value: 100, icon: 'map-marker', color: 'success' }
      ],

      chartData: {
        labels: ['January', 'February'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [40, 20]
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  }
}
</script>
