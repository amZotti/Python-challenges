

public class MyArray {
	static final int NOT_FOUND = -1; // A constant
	
	// Attributes (just one)
	private double data[];
	
	// Constructor
		MyArray (double data[]) {
			this.data = data.clone(); 
		}
		
	// Getter and setter
	double getItem (int key) {
		return data[key];
	}
	
	void setItem (int key, double value) {
		data[key] = value;
	}
	
	// Search methods
	int linearSearch (double key) {
		for(int i = 0; i < data.length; i++){
			if (key == data[i]){
				return i;
			}
			
		}
		return -1;
	}
	
	int binarySearch (double key) {
		int low = 0, high = data.length - 1;
		while (high >= low) {
			int mid = (int)((low + high) / 2);
			if (key < data[mid])
				high = mid - 1;
			else if (key == data[mid])
				return mid;
			else
				low = mid + 1;
		}
		return NOT_FOUND;
	}
	
	// Check if the array is sorted
	boolean isSorted () {
		for (int i = 0; i < data.length - 1; i++)
			if (data[i] > data[i+1])
				return false;
		return true;
	}
	
	// Sort methods
	void selectionSort () {
		for (int i = 0; i < data.length; i++) {
			int current = i;
			for (int j = i + 1; j < data.length; j++)
				if (data[current] > data[j])
					current = j;
			if (current != i) {
				double temp = data[current];
				data[current] = data[i];
				data[i] = temp;
			}
		}
	}

	void insertionSort () {
		for (int i = 1;i < data.length;i++){
			double currentElement = data[i];
			int k = i - 1;
			while(k>=0 & data[k] > currentElement){
				data[k+1] = data[k];
				k -= 1;
				data[k + 1] = currentElement;
			}
			
			
			
		}
	}
}