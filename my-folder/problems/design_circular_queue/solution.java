class MyCircularQueue {
    public int head;
    public int size;
    public int tail;
    public int[] data;
    
    public MyCircularQueue(int k) {
        data = new int[k];
        head = -1;
        tail = -1;
        size = k;
    }
    
    public boolean enQueue(int value) {
        if(isFull() == true){
            return false;
        }
        if (isEmpty() == true){
            head = 0;
        }
        tail = (tail + 1) % size;
        data[tail] = value;
        return true;
    }
            
    public boolean deQueue() {
        if(isEmpty() == true){
            return false;
        }
        if (head == tail){
            head = -1;
            tail = -1;
            return true;
        }
        head = (head + 1) % size;
        return true;
    }
    
    public int Front() {
        if (isEmpty() == true){
            return -1;
        }
        return data[head];
    }
    
    public int Rear() {
        if (isEmpty() == true){
            return -1;
        }
        return data[tail];
    }
    
    public boolean isEmpty() {
        return head == -1;
    }
    
    public boolean isFull() {
        return ((tail + 1) % size) == head;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */