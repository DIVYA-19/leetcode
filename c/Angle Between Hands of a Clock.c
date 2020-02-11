double angleClock(int hour, int minutes){
    double angle;
	    angle = (hour*30 + minutes*0.5) - (minutes*6);
	    if(angle<0){
	        angle = -1 * angle;
	    }
	    
	    if (360-angle < angle){
	        return (360-angle);
	    }

	    return(angle);

}
