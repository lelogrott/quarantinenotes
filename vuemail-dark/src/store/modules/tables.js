export default {
  namespaced: true,
  state: {
    topSearchTable: {
      headers: [
        { text: 'ID#', align: 'center', sortable: false, value: 'id' },
        { text: 'Product Name', align: 'center', sortable: false, value: 'name' },
        { text: 'Dealer', align: 'center', sortable: false, value: 'dealer' },
        { text: 'Price', align: 'center', sortable: false, value: 'price' },
        { text: 'Quantity', align: 'center', sortable: false, value: 'quantity' },
        { text: 'Status', align: 'center', sortable: false, value: 'status' }
      ],
      desserts: [
        {
          id: '01',
          name: 'Samsung Galaxy S8',
          dealer: 'Shamsu',
          price: '$25050',
          quantity: '185',
          status: 'Delivered',
          statusCall: 'delivered'
        },
        {
          id: '02',
          name: 'Samsung Galaxy S8',
          dealer: 'Shamsu',
          price: '$25050',
          quantity: '185',
          status: 'Cancel',
          statusCall: 'cancel'
        },
        {
          id: '03',
          name: 'Samsung Galaxy S8',
          dealer: 'Shamsu',
          price: '$25050',
          quantity: '185',
          status: 'Delivered',
          statusCall: 'delivered'
        },
        {
          id: '04',
          name: 'Samsung Galaxy S8',
          dealer: 'Shamsu',
          price: '$25050',
          quantity: '185',
          status: 'Cancel',
          statusCall: 'cancel'
        },
        {
          id: '05',
          name: 'Samsung Galaxy S8',
          dealer: 'Shamsu',
          price: '$25050',
          quantity: '185',
          status: 'Delivered',
          statusCall: 'delivered'
        }
      ]
    }
  }
}
