
public class ArrayTest {

	public static void main(String[] args) {
		double testData[] = {1,4,32,5,673,145,68,14,757};
		MyArray a = new MyArray (testData);
		System.out.println("a is sorted: " + a.isSorted());
		System.out.println("Index of 5 (linear): " + a.linearSearch(5));
		a.selectionSort();
		System.out.println("a is sorted: " + a.isSorted());
		System.out.println("Index of 5 (linear): " + a.linearSearch(5));
		System.out.println("Index of 6 (linear): " + a.linearSearch(6));
		System.out.println("Index of 5 (binary): " + a.binarySearch(5));
		System.out.println("Index of 6 (binary): " + a.binarySearch(6));
		
		MyArray b = new MyArray (testData);
		System.out.println("b is sorted: " + b.isSorted());
		b.insertionSort();		
		System.out.println("b is sorted: " + b.isSorted());
	}

}