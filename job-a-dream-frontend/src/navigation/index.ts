import board from './board'
import companys from './companys'
import home from './home'
import jobs from './jobs'
import type { HorizontalNavItems } from '@layouts/types'

export default [...home, ...companys, ...jobs, ...board] as HorizontalNavItems
