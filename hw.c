#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Tustin 변환 수행
void tustinTransform(double *num, double *den, double *numZ, double *denZ, double T, int K) {
    double alpha = 2.0 / T;

    // Tustin 변환 적용
    numZ[0] = K * (num[0] * alpha + num[1]);
    numZ[1] = K * (-num[0] * alpha + num[1]);
    denZ[0] = den[0] * alpha + den[1];
    denZ[1] = -den[0] * alpha + den[1];

    // 정규화
    double normFactor = denZ[0];
    for (int i = 0; i < 2; i++) {
        numZ[i] /= normFactor;
        denZ[i] /= normFactor;
    }
}

// Matched Pole-Zero 변환 수행
void matchedPoleZeroTransform(double *num, double *den, double *numZ, double *denZ, double T, int K) {
    double alpha = exp(-den[1] * T); // 분모의 극점 매핑
    double beta = exp(-num[1] * T); // 분자의 영점 매핑
    // Matched Pole-Zero 변환 결과
    numZ[0] = num[0] * K;            
    numZ[1] = -beta * K;    
    denZ[0] = 1.0;               
    denZ[1] = -alpha;            


}
void printPolynomial(const char *label, double *num, double *den) {
    printf("%s:\n", label);
    printf("Numerator: %.5fz^-0 + %.5fz^-1\n", num[0], num[1]);
    printf("Denominator: 1.00000z^-0 + %.5fz^-1\n", den[1]);
}
int main(void) {
    double T; // 샘플링 시간
    double num[2], den[2]; // 연속시간 전달 함수 계수
    double numTustin[2] = {0}, denTustin[2] = {0};
    double numMPZ[2] = {0}, denMPZ[2] = {0};
    int K; // DC gain
    // 입력
    printf("Enter K: ");
    scanf("%d", &K);
    printf("Enter numerator coefficients (b0 b1): ");
    scanf("%lf %lf", &num[0], &num[1]);
    printf("Enter denominator coefficients (a0 a1): ");
    scanf("%lf %lf", &den[0], &den[1]);
    printf("Enter sampling time T: ");
    scanf("%lf", &T);

    // 변환 수행
    tustinTransform(num, den, numTustin, denTustin, T, K);
    matchedPoleZeroTransform(num, den, numMPZ, denMPZ, T, K);

    // 결과 출력
    printPolynomial("Tustin Transform", numTustin, denTustin);
    printf("\n");
    printPolynomial("Matched Pole-Zero Transform", numMPZ, denMPZ);

    return 0;
}
