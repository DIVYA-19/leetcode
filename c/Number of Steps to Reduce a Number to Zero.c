int numberOfSteps (int num){
    int count = 0;
	while(num){
		if(num%2 != 0){
			count++;
			num = num - 1;
		}
		if (num>0){
			num = num/2;
			count++;
		}
	}
	return count;
}
