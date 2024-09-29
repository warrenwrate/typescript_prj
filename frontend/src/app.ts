// app.ts
interface Item {
    id: number;
    name: string;
}

const fetchApiData = async () => {
    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts');
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error('Error fetching API:', error);
    }
  };
  
  fetchApiData();


async function fetchItems(): Promise<void> {
    try {
        const response = await fetch('http://localhost:5120/api/items');
        const items: Item[] = await response.json();
        const itemList = document.getElementById('item-list');
        
        if (itemList) {
            itemList.innerHTML = items.map(item => `<li>${item.name}</li>`).join('');
        } else {
            console.error('Element with id "item-list" not found');
        }
    } catch (error) {
        console.error('Error fetching items:', error);
    }
}

document.addEventListener('DOMContentLoaded', fetchItems);