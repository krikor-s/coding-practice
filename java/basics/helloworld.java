public class helloworld {
    public static void main(String[] args){
        System.out.println("Hello, Krikor");
    
    int[] numbers = {1,2,3,4,5};

    for (int n : numbers) {
        System.out.println(n);

    }
    System.out.println("Sum: " + sumArray(numbers));
    }
    public static int sumArray(int[] arr){
        int total = 0;
        for (int n : arr){
            total += n;
        }
        return total;
    }
}