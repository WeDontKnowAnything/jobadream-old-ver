<script setup lang="ts">
import ChartJsBarChart from '@/views/charts/chartjs/ChartJsBarChart.vue'
import ChartJsHorizontalBarChart from '@/views/charts/chartjs/ChartJsHorizontalBarChart.vue'
import ChartJsPolarAreaChart from '@/views/charts/chartjs/ChartJsPolarAreaChart.vue'
import ChartJsRadarChart from '@/views/charts/chartjs/ChartJsRadarChart.vue'
import type { ChartJsCustomColors } from '@/views/charts/chartjs/types'

const chartJsCustomColors: ChartJsCustomColors = {
  white: '#fff',
  yellow: '#ffe802',
  primary: '#836af9',
  areaChartBlue: '#2c9aff',
  barChartYellow: '#ffcf5c',
  polarChartGrey: '#4f5d70',
  polarChartInfo: '#299aff',
  lineChartYellow: '#d4e157',
  polarChartGreen: '#28dac6',
  lineChartPrimary: '#9e69fd',
  lineChartWarning: '#ff9800',
  horizontalBarInfo: '#26c6da',
  polarChartWarning: '#ff8131',
  scatterChartGreen: '#28c76f',
  warningShade: '#ffbd1f',
  areaChartBlueLight: '#84d0ff',
  areaChartGreyLight: '#edf1f4',
  scatterChartWarning: '#ff9f43',
}
</script>

<template>
  <VRow id="chartjs-wrapper">
    <!-- 👉 Radar Chart -->
    <VCol
      cols="12"
      md="6"
    >
      <VCard title="Radar Chart">
        <VCardText>
          <ChartJsRadarChart />
        </VCardText>
      </VCard>
    </VCol>

    <!-- 👉 Average Skills Polar Area Chart -->
    <VCol
      cols="12"
      md="6"
    >
      <VCard title="Average Skills">
        <VCardText>
          <ChartJsPolarAreaChart :colors="chartJsCustomColors" />
        </VCardText>
      </VCard>
    </VCol>
    <!-- 👉 Latest Statistics -->
    <VCol
      cols="12"
      md="6"
    >
      <VCard>
        <VCardItem class="d-flex flex-wrap justify-space-between gap-4">
          <VCardTitle>Latest Statistics</VCardTitle>

          <template #append>
            <div class="date-picker-wrapper">
              <AppDateTimePicker
                model-value="2022-06-09"
                prepend-inner-icon="tabler-calendar"
                density="compact"
                placeholder="Select Date"
                :config="$vuetify.display.smAndDown ? { position: 'auto center' } : { position: 'auto right' }"
              />
            </div>
          </template>
        </VCardItem>

        <VCardText>
          <ChartJsBarChart :colors="chartJsCustomColors" />
        </VCardText>
      </VCard>
    </VCol>

    <!-- 👉 Balance Horizontal Bar Chart -->
    <VCol
      cols="12"
      md="6"
    >
      <VCard>
        <VCardItem class="d-flex flex-wrap justify-space-between gap-4">
          <VCardTitle>Balance</VCardTitle>
          <VCardSubtitle>$74,123</VCardSubtitle>

          <template #append>
            <div class="date-picker-wrapper">
              <AppDateTimePicker
                model-value="2022-06-09"
                prepend-inner-icon="tabler-calendar"
                density="compact"
                placeholder="Select Date"
                :config="$vuetify.display.smAndDown ? { position: 'auto center' } : { position: 'auto right' }"
              />
            </div>
          </template>
        </VCardItem>

        <VCardText>
          <ChartJsHorizontalBarChart :colors="chartJsCustomColors" />
        </VCardText>
      </VCard>
    </VCol>
  </VRow>
</template>
